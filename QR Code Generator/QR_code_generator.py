# Method : 1
import qrcode
url = input("Enter Text or URL: ")
img = qrcode.make(url)
img.save("qrcode.png")
print("QR code created successfully.")

# Method : 2
import qrcode
counter = 1   
while True:
    print("\n--- QR Code Generator ---")
    name = input("Enter name of QR code: ").strip()
    url = input("Enter URL or Text: ").strip()
    filename = f"{name}_{counter}.png"   # file name with counter
    # Generate QR code
    img = qrcode.make(url)
    img.save(filename)
    print(f"\nQR code '{filename}' successfully created!")
    counter += 1   # next file number
    choice = input("\nDo you want to generate another QR code?(yes/no): ").lower().strip()
    if choice != "yes":
        print("Thank you!")
        break
