import requests
import json

reviews = [
  {"name": "Ali", "review": "The shirt is good, delivery was late."},
  {"name": "Sara", "review": "Really bad quality, I want a refund."},
  {"name": "John", "review": "Excellent service, I’m happy."},
  {"name": "Karim", "review": "Package arrived broken."}
]
with open("reviews.json", "w") as f:
    json.dump(reviews, f, indent=4)
complaints = [review for review in reviews if any(word in review["review"].lower() for word in ["bad", "broken", "late", "refund"])]
for complaint in complaints:
    print(f"Complaint from {complaint['name']}: {complaint['review']}")
with open("complaints.json", "w") as f:
    json.dump(complaints, f, indent=4)
print(f"Total reviews: {len(reviews)}")
print(f"Total complaints: {len(complaints)}")
print(f"Complaint percentage: {len(complaints)/len(reviews)*100:.2f}%")
print("you can find more details in the complaints.json file.")