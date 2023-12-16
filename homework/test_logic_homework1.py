def bounce(initial_height, count, total_cm):
    if count <= 0:
       return total_cm
    current_travel_distance = initial_height + (initial_height // 2)
    print(f"第{count}次：{current_travel_distance:.2f} 公分")
    total_cm += current_travel_distance
    initial_height /= 2
    return bounce(initial_height, count - 1,total_cm)
    
def main():
    print("總共：{total}公分".format(total=bounce(100, 10, 0)))

if __name__ == "__main__":
    main()