def enrollment_stats(universities):
    students = [uni[1] for uni in universities]
    tuitionFees = [uni[2] for uni in universities]
    return students, tuitionFees

def mean(values):
    return sum(values) / len(values) if values else 0

def median(values):
    sortedValues = sorted(values)
    n = len(sortedValues)
    if n == 0:
        return 0
    if n % 2 == 1:
        return sortedValues[n // 2]
    else:
        return (sortedValues[n // 2 - 1] + sortedValues[n // 2]) / 2
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
students, tuition_fees = enrollment_stats(universities)
total_students = sum(students)
total_tuition = sum(tuition_fees)
student_mean = mean(students)
student_median = median(students)
tuition_mean = mean(tuition_fees)
tuition_median = median(tuition_fees)
    
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print("\n")
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}")
print("\n")
print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
