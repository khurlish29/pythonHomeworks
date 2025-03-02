import csv
def calculate_average_grades(input_file, output_file):
    subjects = {}
    counts = {}
    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            subject = row['Subject']
            grade = int(row['Grade'])
            subjects[subject] = subjects.get(subject, 0) + grade
            counts[subject] = counts.get(subject, 0) + 1
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject", "Average Grade"])
        for subject in subjects:
            writer.writerow([subject, subjects[subject] / counts[subject]])