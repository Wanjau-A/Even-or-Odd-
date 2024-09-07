def main():
    num = int(input("Enter a number: "))
    it_is = compute_divisiibility(num)
    print(it_is)

def compute_divisiibility(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
if __name__ == "__main__":
    main()
