student={
    "name":"Amit",
    "age":12,
    "course":"Engineering"
    }

print(student["name"])
student["age"]=22
student["city"]="bc road"
print(student)
#mark
marks={"maths":50,"english":45,"social":56}
print(marks.get("maths"))
print(marks)
for subject,score in marks.items():
 print(subject,score)

#update
marks["maths"]=90
print(marks)

  #remove  value
remove_score=marks.pop("english")
print(marks)

 #example
purchase={
     "alice":150,
     "bob":200,
     "charlie":300
     }
 
for name ,amount in  purchase.items():
    print(f"{name} spent ${amount}")


    
