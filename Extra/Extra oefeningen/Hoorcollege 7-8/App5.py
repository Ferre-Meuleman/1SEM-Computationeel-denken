array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 3, 4, 5]

def equals(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

def main():
    print(equals(array1, array2))  # Verwachte output: False
    
if __name__ == "__main__":
    main()