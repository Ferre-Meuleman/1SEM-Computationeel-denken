N = int(input("Geef N (zoek tot en met N): "))

cube_root_limit = int(N ** (1/3))
while (cube_root_limit + 1) ** 3 <= N:
    cube_root_limit += 1
while cube_root_limit ** 3 > N:
    cube_root_limit -= 1

results = {}
for first_num in range(1, cube_root_limit + 1):
    for second_num in range(first_num + 1, cube_root_limit + 1):
        sum_of_cubes = first_num**3 + second_num**3
        if sum_of_cubes > N:
            continue

        for third_num in range(1, cube_root_limit + 1):
            for fourth_num in range(third_num + 1, cube_root_limit + 1):
                # Skip if any numbers are reused
                if len({first_num, second_num, third_num, fourth_num}) < 4:
                    continue

                # Check if the sums match
                if sum_of_cubes == third_num**3 + fourth_num**3:
                    # Ensure unique pairs are added
                    pair1, pair2 = (
                        first_num, second_num), (third_num, fourth_num)
                    if pair1 < pair2:
                        results.setdefault(
                            sum_of_cubes, []).append((pair1, pair2))

if not results:
    print("Geen getallen ≤", N,
          "gevonden die als twee verschillende sommen van twee derdemachten geschreven kunnen worden.")
else:
    for sum_of_cubes in sorted(results):
        print(
            f"\n{sum_of_cubes} kan als som van twee derdemachten op de volgende verschillende manieren:")
        for (pair1, pair2) in results[sum_of_cubes]:
            first_num, second_num = pair1
            third_num, fourth_num = pair2
            print(
                f"  {first_num}^3 + {second_num}^3 = {first_num**3} + {second_num**3} = {sum_of_cubes}")
            print(
                f"  {third_num}^3 + {fourth_num}^3 = {third_num**3} + {fourth_num**3} = {sum_of_cubes}")
