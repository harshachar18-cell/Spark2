"""
Student Marks Analyzer using Apache Spark
This application analyzes student marks data using PySpark
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min, count, sum, round, when
from pyspark.sql.window import Window
import pyspark.sql.functions as F
import sys


class StudentMarksAnalyzer:
    """Main class for analyzing student marks"""
    
    def __init__(self, app_name="StudentMarksAnalyzer"):
        """Initialize Spark Session"""
        self.spark = SparkSession.builder \
            .appName(app_name) \
            .master("local[*]") \
            .getOrCreate()
        
        self.spark.sparkContext.setLogLevel("ERROR")
        print(f"✓ Spark Session initialized: {app_name}")
    
    def load_data(self, file_path):
        """Load student marks data from CSV"""
        try:
            self.df = self.spark.read.csv(
                file_path,
                header=True,
                inferSchema=True
            )
            print(f"✓ Data loaded successfully from {file_path}")
            print(f"  Total records: {self.df.count()}")
            return self.df
        except Exception as e:
            print(f"✗ Error loading data: {str(e)}")
            sys.exit(1)
    
    def show_data_overview(self):
        """Display basic data overview"""
        print("\n" + "="*80)
        print("DATA OVERVIEW")
        print("="*80)
        print("\nSample Data:")
        self.df.show(10, truncate=False)
        
        print("\nSchema:")
        self.df.printSchema()
        
        print("\nData Summary:")
        self.df.describe().show()
    
    def calculate_total_and_percentage(self):
        """Calculate total marks and percentage for each student"""
        print("\n" + "="*80)
        print("STUDENT PERFORMANCE - TOTAL MARKS & PERCENTAGE")
        print("="*80)
        
        # Calculate total marks
        self.df = self.df.withColumn(
            "Total_Marks",
            col("Math") + col("Science") + col("English") + 
            col("History") + col("Geography")
        )
        
        # Calculate percentage
        self.df = self.df.withColumn(
            "Percentage",
            round((col("Total_Marks") / 500) * 100, 2)
        )
        
        # Determine grade
        self.df = self.df.withColumn(
            "Grade",
            when(col("Percentage") >= 90, "A+")
            .when(col("Percentage") >= 80, "A")
            .when(col("Percentage") >= 70, "B")
            .when(col("Percentage") >= 60, "C")
            .when(col("Percentage") >= 50, "D")
            .otherwise("F")
        )
        
        self.df.select(
            "Student_ID", "Name", "Total_Marks", "Percentage", "Grade"
        ).orderBy(col("Total_Marks").desc()).show(20, truncate=False)
        
        return self.df
    
    def subject_wise_analysis(self):
        """Analyze performance subject-wise"""
        print("\n" + "="*80)
        print("SUBJECT-WISE ANALYSIS")
        print("="*80)
        
        subjects = ["Math", "Science", "English", "History", "Geography"]
        
        for subject in subjects:
            stats = self.df.agg(
                avg(col(subject)).alias("Average"),
                max(col(subject)).alias("Maximum"),
                min(col(subject)).alias("Minimum"),
                count(col(subject)).alias("Count")
            ).collect()[0]
            
            print(f"\n{subject}:")
            print(f"  Average: {stats['Average']:.2f}")
            print(f"  Maximum: {stats['Maximum']}")
            print(f"  Minimum: {stats['Minimum']}")
            print(f"  Count: {stats['Count']}")
    
    def top_performers(self, n=10):
        """Display top N performers"""
        print("\n" + "="*80)
        print(f"TOP {n} PERFORMERS")
        print("="*80)
        
        self.df.select(
            "Student_ID", "Name", "Total_Marks", "Percentage", "Grade"
        ).orderBy(col("Total_Marks").desc()).limit(n).show(n, truncate=False)
    
    def grade_distribution(self):
        """Show grade distribution"""
        print("\n" + "="*80)
        print("GRADE DISTRIBUTION")
        print("="*80)
        
        grade_dist = self.df.groupBy("Grade").agg(
            count("*").alias("Student_Count")
        ).orderBy(col("Grade"))
        
        grade_dist.show()
        
        # Calculate percentage distribution
        total_students = self.df.count()
        grade_dist.withColumn(
            "Percentage",
            round((col("Student_Count") / total_students) * 100, 2)
        ).show()
    
    def class_wise_analysis(self):
        """Analyze performance class-wise"""
        print("\n" + "="*80)
        print("CLASS-WISE ANALYSIS")
        print("="*80)
        
        class_stats = self.df.groupBy("Class").agg(
            count("*").alias("Total_Students"),
            round(avg("Total_Marks"), 2).alias("Avg_Total_Marks"),
            round(avg("Percentage"), 2).alias("Avg_Percentage"),
            max("Total_Marks").alias("Max_Marks"),
            min("Total_Marks").alias("Min_Marks")
        ).orderBy("Class")
        
        class_stats.show(truncate=False)
    
    def subject_toppers(self):
        """Find toppers in each subject"""
        print("\n" + "="*80)
        print("SUBJECT TOPPERS")
        print("="*80)
        
        subjects = ["Math", "Science", "English", "History", "Geography"]
        
        for subject in subjects:
            topper = self.df.orderBy(col(subject).desc()).select(
                "Student_ID", "Name", "Class", subject
            ).first()
            
            print(f"\n{subject} Topper:")
            print(f"  Name: {topper['Name']} (ID: {topper['Student_ID']})")
            print(f"  Class: {topper['Class']}")
            print(f"  Marks: {topper[subject]}")
    
    def students_needing_improvement(self, threshold=50):
        """Identify students who need improvement"""
        print("\n" + "="*80)
        print(f"STUDENTS NEEDING IMPROVEMENT (Percentage < {threshold}%)")
        print("="*80)
        
        struggling_students = self.df.filter(col("Percentage") < threshold).select(
            "Student_ID", "Name", "Class", "Total_Marks", "Percentage", "Grade"
        ).orderBy(col("Percentage"))
        
        count = struggling_students.count()
        print(f"\nTotal students needing improvement: {count}")
        
        if count > 0:
            struggling_students.show(20, truncate=False)
        else:
            print("All students are performing well!")
    
    def save_results(self, output_path):
        """Save analysis results to CSV"""
        try:
            self.df.coalesce(1).write.mode("overwrite").csv(
                output_path,
                header=True
            )
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
    
    def stop(self):
        """Stop Spark session"""
        self.spark.stop()
        print("\n✓ Spark session stopped")


def main():
    """Main execution function"""
    print("\n" + "="*80)
    print("STUDENT MARKS ANALYZER - APACHE SPARK")
    print("="*80 + "\n")
    
    # Initialize analyzer
    analyzer = StudentMarksAnalyzer()
    
    # Define file paths
    input_file = "student_marks_data.csv"
    output_file = "analyzed_results"
    
    try:
        # Run complete analysis
        analyzer.run_complete_analysis(input_file, output_file)
    except Exception as e:
        print(f"\n✗ Error during analysis: {str(e)}")
    finally:
        # Stop Spark session
        analyzer.stop()


if __name__ == "__main__":
    main()
