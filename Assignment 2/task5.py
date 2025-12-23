valid_letters = set("ABCEHKMOPRTXY")

n = int(input().strip())
plates = [input().strip() for _ in range(n)]

for plate in plates:
    if len(plate) != 6:
        print("No")
        continue

    if (plate[0] in valid_letters and
        plate[1].isdigit() and
        plate[2].isdigit() and
        plate[3].isdigit() and
        plate[4] in valid_letters and
        plate[5] in valid_letters):
        print("Yes")
    else:
        print("No")