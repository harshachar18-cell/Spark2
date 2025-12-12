# Setup Guide - Student Marks Analyzer

This project provides **TWO versions** of the Student Marks Analyzer:

## 📦 Quick Start (No Java Required)

If you want to run the analysis immediately without installing Java and Spark:

### Using Pandas Version

```bash
# Install pandas (lightweight)
pip install pandas

# Run the analyzer
python student_marks_analyzer_pandas.py
```

This version provides the same analysis functionality using Pandas instead of Spark.

---

## 🚀 Full Apache Spark Version (Recommended for Learning)

For the complete Apache Spark experience, you need to install Java first.

### Step 1: Install Java

#### Windows:

1. **Download Java 8 or 11:**
   - Java 8: https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html
   - Or use OpenJDK: https://adoptium.net/

2. **Install Java:**
   - Run the installer
   - Note the installation path (e.g., `C:\Program Files\Java\jdk-11.0.x`)

3. **Set JAVA_HOME Environment Variable:**
   
   **Option A - Via PowerShell (Administrator):**
   ```powershell
   # Replace with your actual Java path
   [System.Environment]::SetEnvironmentVariable("JAVA_HOME", "C:\Program Files\Java\jdk-11.0.x", "Machine")
   [System.Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";%JAVA_HOME%\bin", "Machine")
   ```

   **Option B - Via System Settings:**
   - Right-click "This PC" → Properties
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System Variables", click "New"
   - Variable name: `JAVA_HOME`
   - Variable value: `C:\Program Files\Java\jdk-11.0.x` (your Java path)
   - Click OK
   - Find `Path` variable, click Edit
   - Add new entry: `%JAVA_HOME%\bin`
   - Click OK on all windows

4. **Verify Installation:**
   ```bash
   # Restart your terminal/PowerShell
   java -version
   ```

#### macOS:

```bash
# Install using Homebrew
brew install openjdk@11

# Add to shell profile
echo 'export JAVA_HOME=$(/usr/libexec/java_home)' >> ~/.zshrc
source ~/.zshrc

# Verify
java -version
```

#### Linux:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install openjdk-11-jdk

# Set JAVA_HOME
echo 'export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64' >> ~/.bashrc
source ~/.bashrc

# Verify
java -version
```

### Step 2: Install PySpark

```bash
# Install PySpark
pip install pyspark==3.5.0 py4j==0.10.9.7

# Or use requirements.txt
pip install -r requirements.txt
```

### Step 3: Run the Spark Version

```bash
python student_marks_analyzer.py
```

---

## 📊 Which Version Should I Use?

| Feature | Pandas Version | Spark Version |
|---------|---------------|---------------|
| Installation | ✅ Easy (no Java) | ⚠️ Requires Java |
| Setup Time | 1 minute | 10-15 minutes |
| Performance (100 rows) | ⚡ Fast | ⚡ Fast |
| Performance (1M+ rows) | 🐌 Slow | ⚡ Very Fast |
| Learning Spark | ❌ No | ✅ Yes |
| Production Ready | For small data | For big data |

### Recommendations:

- **Just want to see results?** → Use Pandas version
- **Learning Apache Spark?** → Use Spark version (worth the setup!)
- **Small dataset (< 10K rows)?** → Either version works
- **Large dataset (> 100K rows)?** → Spark version recommended

---

## 🔧 Troubleshooting

### "Java not found" Error

**Problem:**
```
Java not found and JAVA_HOME environment variable is not set.
```

**Solutions:**
1. Install Java (see Step 1 above)
2. Restart your terminal/IDE after setting JAVA_HOME
3. Verify: `echo %JAVA_HOME%` (Windows) or `echo $JAVA_HOME` (Mac/Linux)
4. Verify: `java -version`

### "Module not found: pyspark"

**Solution:**
```bash
pip install pyspark==3.5.0
```

### "File not found: student_marks_data.csv"

**Solution:**
- Ensure you're running the script from the `spark` directory
- Check that `student_marks_data.csv` exists in the same folder

### Slow Installation on Windows

**Solution:**
- PySpark is ~317MB, so download takes time
- Be patient during `pip install pyspark`
- Consider using a faster internet connection

---

## 📝 File Structure

```
spark/
│
├── student_marks_analyzer.py          # Main Spark version
├── student_marks_analyzer_pandas.py   # Pandas version (no Java)
├── student_marks_data.csv             # Sample dataset (100 students)
├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
└── SETUP_GUIDE.md                     # This file
```

---

## 🎯 Next Steps

1. **Run the analysis** (choose your version)
2. **Explore the results** in the console output
3. **Modify the dataset** - add your own student data
4. **Customize the analysis** - adjust grading criteria, thresholds
5. **Learn Spark** - if you installed the Spark version, experiment with the code!

---

## 💡 Quick Test

After installation, verify everything works:

```bash
# Test Pandas version (no Java needed)
python student_marks_analyzer_pandas.py

# Test Spark version (requires Java)
python student_marks_analyzer.py
```

Both should produce comprehensive analysis output!

---

## 📚 Additional Resources

- **Apache Spark Documentation:** https://spark.apache.org/docs/latest/
- **PySpark Guide:** https://spark.apache.org/docs/latest/api/python/
- **Pandas Documentation:** https://pandas.pydata.org/docs/

---

**Need Help?** Make sure:
- ✅ Java is installed and JAVA_HOME is set (for Spark version)
- ✅ Python 3.7+ is installed
- ✅ pip packages are installed
- ✅ You're in the correct directory
- ✅ CSV file exists

Happy Analyzing! 🎉
