
import csv

def file_to_csv(mylist):
    
    file_csv = open("Student_Data.csv", mode = 'a', newline='')
    file_csv_writer = csv.writer(file_csv)

    if file_csv.tell() == 0:
        file_csv_writer.writerow(["Name", "Age", "Contact Number", "Email-Id"])

    file_csv_writer.writerow(mylist)
    file_csv.close()

if __name__ == "__main__":
    
    condition = True

    while(condition):
        student_data = (input("Enter the student details in the format: Name Age Contact Number Email-Id\n"))

        student_info = student_data.split(" ")

        print("The entered information is:\nName:{} \nAge:{} \nContact Number:{} \nEmail-Id:{}".format(student_info[0], student_info[1], student_info[2], student_info[3]))

        check1 = input("Is the information you entered correct? Choose from yes/no.\n ")
    
        if check1 == "yes":
            file_to_csv(student_info)
    
            check2 = input("Would you like to make another student entry? Choose from yes/no.\n")
            if check2 == "yes":
                condition == True
            elif check1 == "no":
                condition == False
                
    
        elif check1 == "no":
            print("Enter the correct information:\n")


