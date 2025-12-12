# Student Marks Analyzer - Apache Spark

A comprehensive student marks analysis system built with Apache Spark that analyzes student performance across multiple subjects.

## Features

- **Data Loading & Overview**: Load student marks data from CSV files
- **Performance Calculation**: Calculate total marks, percentage, and assign grades
- **Subject-wise Analysis**: Analyze performance across Math, Science, English, History, and Geography
- **Top Performers**: Identify and rank top-performing students
- **Grade Distribution**: Visualize grade distribution across the student body
- **Class-wise Analysis**: Compare performance across different classes
- **Subject Toppers**: Find the highest scorers in each subject
- **Improvement Tracking**: Identify students who need additional support
- **Results Export**: Save analysis results for further use

## Project Structure

```
spark/
│
├── student_marks_analyzer.py   # Main Spark application
├── student_marks_data.csv      # Sample student marks dataset (100 students)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Prerequisites

- Python 3.7 or higher
- Java 8 or higher (required for Apache Spark)
- Apache Spark (installed via pip with PySpark)

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Java installation:**
   ```bash
   java -version
   ```
   If Java is not installed, download and install from [Oracle](https://www.oracle.com/java/technologies/downloads/) or [OpenJDK](https://openjdk.org/).

## Usage

### Run the Analysis

```bash
python student_marks_analyzer.py
```

### What the Application Does

The application performs the following analyses:

1. **Data Overview**: Displays sample data and schema
2. **Performance Metrics**: Calculates total marks and percentages
3. **Grading**: Assigns grades based on performance
   - A+ : 90% and above
   - A  : 80-89%
   - B  : 70-79%
   - C  : 60-69%
   - D  : 50-59%
   - F  : Below 50%
4. **Subject-wise Statistics**: Average, maximum, and minimum marks per subject
5. **Top Performers**: Lists top 10 students
6. **Grade Distribution**: Shows how many students fall in each grade category
7. **Class-wise Comparison**: Compares performance across classes (10A, 10B, 10C)
8. **Subject Toppers**: Identifies highest scorers in each subject
9. **Improvement List**: Flags students scoring below 50%

### Sample Output

The application generates comprehensive console output including:

```
================================================================================
STUDENT MARKS ANALYZER - APACHE SPARK
================================================================================

✓ Spark Session initialized: StudentMarksAnalyzer
✓ Data loaded successfully from student_marks_data.csv
  Total records: 100

================================================================================
DATA OVERVIEW
================================================================================

[Sample data, schema, and statistics]

================================================================================
STUDENT PERFORMANCE - TOTAL MARKS & PERCENTAGE
================================================================================

[Student rankings with total marks, percentage, and grades]

================================================================================
SUBJECT-WISE ANALYSIS
================================================================================

[Average, maximum, minimum marks for each subject]

... and more analyses
```

## Dataset Description

The sample dataset (`student_marks_data.csv`) contains:
- **100 students** across 3 classes (10A, 10B, 10C)
- **5 subjects**: Math, Science, English, History, Geography
- Each subject is marked out of 100
- Total marks out of 500

### Data Columns:
- `Student_ID`: Unique identifier for each student
- `Name`: Student name
- `Class`: Class section (10A, 10B, 10C)
- `Math`: Math marks (0-100)
- `Science`: Science marks (0-100)
- `English`: English marks (0-100)
- `History`: History marks (0-100)
- `Geography`: Geography marks (0-100)

## Customization

### Modify the Input File

Edit the file path in `student_marks_analyzer.py`:
```python
input_file = "your_data.csv"
```

### Change Grading Criteria

Modify the grading logic in the `calculate_total_and_percentage()` method:
```python
self.df = self.df.withColumn(
    "Grade",
    when(col("Percentage") >= 90, "A+")
    .when(col("Percentage") >= 80, "A")
    # Modify these thresholds as needed
)
```

### Adjust Analysis Parameters

- Change the number of top performers: `analyzer.top_performers(20)`
- Modify improvement threshold: `analyzer.students_needing_improvement(60)`

## Output Files

The application saves results to the `analyzed_results` directory as CSV files with complete analysis data.

## Technical Details

### Technologies Used
- **Apache Spark**: Distributed data processing
- **PySpark**: Python API for Spark
- **Spark SQL**: For data manipulation and analysis
- **Spark DataFrames**: For structured data operations

### Spark Operations Used
- Data loading and schema inference
- Column transformations
- Aggregations (avg, max, min, count)
- Filtering and sorting
- Grouping and window functions
- Conditional logic (when/otherwise)

## Troubleshooting

### Java not found
```
Error: JAVA_HOME is not set
```
**Solution**: Install Java and set JAVA_HOME environment variable.

### Module not found
```
ModuleNotFoundError: No module named 'pyspark'
```
**Solution**: Run `pip install -r requirements.txt`

### File not found
```
Error loading data: student_marks_data.csv not found
```
**Solution**: Ensure the CSV file is in the same directory as the Python script.

## Future Enhancements

- Add visualization using Matplotlib/Plotly
- Implement trend analysis across multiple terms
- Add support for multiple schools/departments
- Create a web dashboard using Flask/Django
- Add machine learning for performance prediction
- Export results to Excel format

## License

This project is open source and available for educational purposes.

## Author

Created as a demonstration of Apache Spark for student data analysis.

---

**Note**: This is a sample project for learning Apache Spark. The data is randomly generated for demonstration purposes.
