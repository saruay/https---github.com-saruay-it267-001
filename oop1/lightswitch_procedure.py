#เปิด
def turnon():
    global switch_status
    switch_status = True #เปิด
#ปิด
def turnoff():
    global switch_status
    switch_status = False #ปิด

switch_status = False #ปิด

print(f"Status = {switch_status}")
turnon()
print(f"Status = {switch_status}")
turnoff()
print(f"Status = {switch_status}")
turnoff()
print(f"Status = {switch_status}")
