from flask import Flask, render_template, request, jsonify
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our analyzer modules
try:
    from student_marks_analyzer_pandas import StudentMarksAnalyzerPandas
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False

try:
    from student_marks_analyzer import StudentMarksAnalyzer
    SPARK_AVAILABLE = True
except ImportError:
    SPARK_AVAILABLE = False

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', 
                         pandas_available=PANDAS_AVAILABLE,
                         spark_available=SPARK_AVAILABLE)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Get the analysis type and dataset size from the form
        analysis_type = request.form.get('analysis_type', 'pandas')
        dataset_size = request.form.get('dataset_size', '100')
        
        # Determine which dataset file to use
        if dataset_size == '200':
            data_file = 'student_marks_data_200.csv'
        else:
            data_file = 'student_marks_data.csv'
        
        if analysis_type == 'pandas' and PANDAS_AVAILABLE:
            # Run pandas analysis
            analyzer = StudentMarksAnalyzerPandas()
            analyzer.load_data(data_file)
            analyzer.calculate_total_and_percentage()
            
            # Prepare results
            results = {
                'success': True,
                'message': f'Analysis completed successfully with {dataset_size} records',
                'top_performers': analyzer.df.head(10).to_dict('records'),
                'subject_stats': {},
                'grade_distribution': {},
                'total_students': len(analyzer.df)
            }
            
            # Add subject statistics
            subjects = ["Math", "Science", "English", "History", "Geography"]
            for subject in subjects:
                results['subject_stats'][subject] = {
                    'average': float(analyzer.df[subject].mean()),
                    'maximum': int(analyzer.df[subject].max()),
                    'minimum': int(analyzer.df[subject].min())
                }
            
            # Add grade distribution
            grade_counts = analyzer.df['Grade'].value_counts().to_dict()
            total_students = len(analyzer.df)
            for grade, count in grade_counts.items():
                results['grade_distribution'][grade] = {
                    'count': count,
                    'percentage': round((count / total_students) * 100, 2)
                }
            
            return jsonify(results)
            
        elif analysis_type == 'spark' and SPARK_AVAILABLE:
            return jsonify({
                'success': False,
                'message': 'Spark version not yet implemented in web interface'
            })
        else:
            return jsonify({
                'success': False,
                'message': f'{analysis_type.capitalize()} version not available'
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error during analysis: {str(e)}'
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)