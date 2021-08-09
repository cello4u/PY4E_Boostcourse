# function1: saving raw information from guest book
def raw_guest_book(guest_book):
    try:
        raw_file = open("guest_book.txt","a", encoding="UTF8")
    except:
        raw_file = open("guest_book.txt","w", encoding="UTF8")
    raw_file.write(guest_book+"\n")
    raw_file.close()

#main command
#input one by one until 'done'
while True:
    raw = input("Insert raw guest book's information by lines(Name,Phone no).\nWhen it is done insert 'done':")
    if raw == 'done' or raw == 'DONE':
        break
    else:
        raw_guest_book(raw)

# open task file
task_file = open("guest_book.txt","r",encoding="UTF8")
# show task file to user
contents=task_file.read()
print("\nBelow list is what you wrote on the file.")
print("-----Raw records of the guest book-----")
print(contents)
print("---------------------------------------")

# find wrong record
task_file = open("guest_book.txt","r",encoding="UTF8")
for line in task_file:
    pos = line.find(",")# , 구분점 위치 확인
    # 이름과 전화번호 구분
    name = line[:pos]
    phone = line[pos+1:].strip()
	# 조건을 만족하면 continue 아니면 출력
    if len(phone) == 13 and phone.find("-") != -1 and phone.startswith("010") == True:
        continue
    else:
        print(f"Person who wrote wrong phone no.: {name}")
        print(f"The wrong phone no.: {phone}")
        print()
