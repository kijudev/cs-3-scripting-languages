def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


start = int(input("from year: "))
end = int(input("to year: "))

leap_years = [year for year in range(start, end + 1) if is_leap(year)]

print(*leap_years, sep="\n")
print("----")
print(f"leap years in range: {len(leap_years)}")
