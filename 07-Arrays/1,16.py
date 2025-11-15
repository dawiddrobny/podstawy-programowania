# Sort the data from lowest to highest value
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
print("Original distances:", distances_traveled)
distances_traveled.sort()
print("Sorted distances (ascending):", distances_traveled)

# Sort the data in descending order, from highest to lowest value
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
print("Original daily temperatures:", daily_temperatures)
daily_temperatures.sort(reverse=True)
print("Sorted daily temperatures (descending):", daily_temperatures)

# Sort the data in ascending order
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
              "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
print("Original file names:", file_names)
file_names.sort()
print("Sorted file names (alphabetical):", file_names)
