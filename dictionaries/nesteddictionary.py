member1= {
    "name" : "plant",
    "instrument": "vocals"

}

member2= {
    "name" : "page",
    "instrument": "guitar"

}

band= {
    "member1": member1,
    "member2": member2
}


print(band)

print(band["member1"]["name"])

