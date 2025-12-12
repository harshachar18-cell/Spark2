"""
Student Marks Analyzer - Pandas Version (No Java Required)
This is a lightweight version using Pandas for quick analysis without Spark installation
"""

import pandas as pd
import sys


class StudentMarksAnalyzerPandas:
    """Pandas-based analyzer for environments without Spark/Java"""
    
    def __init__(self):
        """Initialize the analyzer"""
        print("✓ Pandas Analyzer initialized (No Java required)")
        self.df = None
    
    def load_data(self, file_path):
        """Load student marks data from CSV"""
        try:
            self.df = pd.read_csv(file_path)
            print(f"✓ Data loaded successfully from {file_path}")
            print(f"  Total records: {len(self.df)}")
            return self.df
        except Exception as e:
            print(f"✗ Error loading data: {str(e)}")
            sys.exit(1)
    
    def show_data_overview(self):
        """Display basic data overview"""
        print("\n" + "="*80)
        print("DATA OVERVIEW")
        print("="*80)
        print("\nSample Data (First 10 rows):")
        print(self.df.head(10).to_string(index=False))
        
        print("\n\nData Info:")
        print(self.df.info())
        
        print("\n\nData Summary:")
        print(self.df.describe())
    
    def calculate_total_and_percentage(self):
        """Calculate total marks and percentage for each student"""
        print("\n" + "="*80)
        print("STUDENT PERFORMANCE - TOTAL MARKS & PERCENTAGE")
        print("="*80)
        
        # Calculate total marks
        self.df['Total_Marks'] = (
            self.df['Math'] + self.df['Science'] + self.df['English'] + 
            self.df['History'] + self.df['Geography']
        )
        
        # Calculate percentage
        self.df['Percentage'] = round((self.df['Total_Marks'] / 500) * 100, 2)
        
        # Determine grade
        def assign_grade(percentage):
            if percentage >= 90:
                return "A+"
            elif percentage >= 80:
                return "A"
            elif percentage >= 70:
                return "B"
            elif percentage >= 60:
                return "C"
            elif percentage >= 50:
                return "D"
            else:
                return "F"
        
        self.df['Grade'] = self.df['Percentage'].apply(assign_grade)
        
        # Display results
        result = self.df[['Student_ID', 'Name', 'Total_Marks', 'Percentage', 'Grade']].sort_values(
            by='Total_Marks', ascending=False
        )
        print("\n" + result.head(20).to_string(index=False))
        
        return self.df
    
    def subject_wise_analysis(self):
        """Analyze performance subject-wise"""
        print("\n" + "="*80)
        print("SUBJECT-WISE ANALYSIS")
        print("="*80)
        
        subjects = ["Math", "Science", "English", "History", "Geography"]
        
        for subject in subjects:
            avg_marks = self.df[subject].mean()
            max_marks = self.df[subject].max()
            min_marks = self.df[subject].min()
            count = self.df[subject].count()
            
            print(f"\n{subject}:")
            print(f"  Average: {avg_marks:.2f}")
            print(f"  Maximum: {max_marks}")
            print(f"  Minimum: {min_marks}")
            print(f"  Count: {count}")
    
    def top_performers(self, n=10):
        """Display top N performers"""
        print("\n" + "="*80)
        print(f"TOP {n} PERFORMERS")
        print("="*80)
        
        top_students = self.df[['Student_ID', 'Name', 'Total_Marks', 'Percentage', 'Grade']].sort_values(
            by='Total_Marks', ascending=False
        ).head(n)
        
        print("\n" + top_students.to_string(index=False))
    
    def grade_distribution(self):
        """Show grade distribution"""
        print("\n" + "="*80)
        print("GRADE DISTRIBUTION")
        print("="*80)
        
        grade_dist = self.df.groupby('Grade').size().reset_index(name='Student_Count')
        grade_dist = grade_dist.sort_values('Grade')
        
        print("\n" + grade_dist.to_string(index=False))
        
        # Calculate percentage distribution
        total_students = len(self.df)
        grade_dist['Percentage'] = round((grade_dist['Student_Count'] / total_students) * 100, 2)
        
        print("\n\nGrade Distribution with Percentages:")
        print(grade_dist.to_string(index=False))
    
    def class_wise_analysis(self):
        """Analyze performance class-wise"""
        print("\n" + "="*80)
        print("CLASS-WISE ANALYSIS")
        print("="*80)
        
        class_stats = self.df.groupby('Class').agg({
            'Student_ID': 'count',
            'Total_Marks': ['mean', 'max', 'min'],
            'Percentage': 'mean'
        }).round(2)
        
        class_stats.columns = ['Total_Students', 'Avg_Total_Marks', 'Max_Marks', 'Min_Marks', 'Avg_Percentage']
        class_stats = class_stats.reset_index()
        
        print("\n" + class_stats.to_string(index=False))
    
    def subject_toppers(self):
        """Find toppers in each subject"""
        print("\n" + "="*80)
        print("SUBJECT TOPPERS")
        print("="*80)
        
        subjects = ["Math", "Science", "English", "History", "Geography"]
        
        for subject in subjects:
            topper_idx = self.df[subject].idxmax()
            topper = self.df.loc[topper_idx]
            
            print(f"\n{subject} Topper:")
            print(f"  Name: {topper['Name']} (ID: {topper['Student_ID']})")
            print(f"  Class: {topper['Class']}")
            print(f"  Marks: {topper[subject]}")
    
    def students_needing_improvement(self, threshold=50):
        """Identify students who need improvement"""
        print("\n" + "="*80)
        print(f"STUDENTS NEEDING IMPROVEMENT (Percentage < {threshold}%)")
        print("="*80)
        
        struggling_students = self.df[self.df['Percentage'] < threshold][
            ['Student_ID', 'Name', 'Class', 'Total_Marks', 'Percentage', 'Grade']
        ].sort_values(by='Percentage')
        
        count = len(struggling_students)
        print(f"\nTotal students needing improvement: {count}")
        
        if count > 0:
            print("\n" + struggling_students.to_string(index=False))
        else:
            print("All students are performing well!")
    
    def save_results(self, output_path):
        """Save analysis results to CSV"""
        try:
            self.df.to_csv(output_path, index=False)
            print(f"\n✓ Results saved to {output_path}")
        except Exception as e:
            print(f"✗ Error saving results: {str(e)}")
    
    def run_complete_analysis(self, input_file, output_file=None):
        """Run complete analysis pipeline"""
        # Load data
        self.load_data(input_file)
        
        # Show overview
        self.show_data_overview()
        
        # Calculate totals and percentages
        self.calculate_total_and_percentage()
        
        # Various analyses
        self.subject_wise_analysis()
        self.top_performers(10)
        self.grade_distribution()
        self.class_wise_analysis()
        self.subject_toppers()
        self.students_needing_improvement(50)
        
        # Save results if output path provided
        if output_file:
            self.save_results(output_file)
        
        print("\n" + "="*80)
        print("ANALYSIS COMPLETE")
        print("="*80)


def main():
    """Main execution function"""
    print("\n" + "="*80)
    print("STUDENT MARKS ANALYZER - PANDAS VERSION")
    print("="*80 + "\n")
    
    # Initialize analyzer
    analyzer = StudentMarksAnalyzerPandas()
    
    # Define file paths
    input_file = "student_marks_data.csv"
    output_file = "analyzed_results_pandas.csv"
    
    try:
        # Run complete analysis
        analyzer.run_complete_analysis(input_file, output_file)
    except Exception as e:
        print(f"\n✗ Error during analysis: {str(e)}")


if __name__ == "__main__":
    main()
