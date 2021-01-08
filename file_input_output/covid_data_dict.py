
covid_data={}
f=open("covid_19_india.csv","r")
for lines in f:
    data=lines.rstrip("\n").lower().split(",")
    print(data)
    state=data[3].rstrip("***")
    if state=="telengana":
        state="telangana"

    cured=data[6]
    confrmd_case=data[8]
    death=data[7]
    covid_data[state]={
        "state":state,

        "cured":cured,
        "confrmd_case":confrmd_case,
        "death":death

    }
for k,v in covid_data.items():
    print(k,v)


def print_covid_data(**kwargs):
    state=kwargs["state"]
    if state in covid_data:
        print(state,",",covid_data[state]["confrmd_case"])
    else:
        print("you given invalid state")
print_covid_data(state="kerala")