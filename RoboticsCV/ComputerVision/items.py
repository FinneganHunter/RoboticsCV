if __name__ == "__main__":
    threadObj = threading.Thread(target=video_feed)

    threadObj.start()

    print("\n", threading.main_thread(), " Active Thread")
    print("\nPress Enter To Exit")
    input()
