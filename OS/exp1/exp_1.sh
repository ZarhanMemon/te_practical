#!/bin/bash

file="address_book.txt"

while true
do 
  echo "=============Address Book Menu============="
  echo "1. Create a Adress Book"
  echo "2. View Address Book"
  echo "3. Insert a new record "
  echo "4. Delete a record "
  echo "5. Modify a record"
  echo "6. Exit"
  echo "=========================================="

  echo " Enter your choice : "
  read choice
  
# Create a new address book
  if [ "$choice" -eq 1 ]; then
    > $file
    echo "Address book created"

# View the address book
  elif [ "$choice" -eq 2 ]; then
    
    if [ -f "$file" ]; then
       echo "Address Book Content : "
       cat $file
    else
       echo "File not found"
    fi


# Insert a new record
  elif [ "$choice" -eq 3 ]; then 
   
   echo "New Record :- "

   echo "Enter Name :"
   read name
   echo "Enter Phone :"
   read phone
   echo "Enter City :"
   read city

   echo "$name | $phone | $city" >> $file
   echo "record inserted"


# Delete a record
  elif [ "$choice" -eq 4 ]; then

   echo "Enter the name of the record to delete :"
   read name

    grep -v "^$name |" $file > temp.txt    # grep -v will exclude the line that starts with the name and save the rest to temp.txt
    cp temp.txt $file                     # copy the content of temp in file and del temp.txt
    rm temp.txt
    echo "Record deleted"


# Modify a record
  elif [ "$choice" -eq 5 ]; then

    echo "Enter the name you wnat to modify record : "
    read name

    grep -v "^$name |" $file > temp.txt    # modifying record deleting  from file and save the rest to temp.txt
    cp temp.txt $file
    rm temp.txt

    echo "Enter modify record :- "    #New record is considerd as modify record
    echo "Enter Name :"
    read name
    echo "Enter Phone :"
    read phone
    echo "Enter City :"
    read city

    echo "$name | $phone | $city" >> $file
    echo "Record modified"


# Exit the program
  elif [ "$choice" -eq 6 ]; then
    
    echo "Exiting..."
    exit 0

  else
  echo "Invalid choice redo it."

  fi

done

