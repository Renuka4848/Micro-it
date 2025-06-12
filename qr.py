# In main file
# import script3
# print(script3.sum(1, 3))

import qrcode

def generate_qr_code(upi_url, filename):
    """
    Generate a QR code from a UPI payment URL and save it to a file.
    
    Args:
        upi_url (str): The UPI payment URL.
        filename (str): The filename to save the QR code.
    """
    try:
        # Generate QR code
        img = qrcode.make(upi_url)
        
        # Save QR code to file
        img.save(filename)
        
        # Display QR code
        img.show()
        
        print(f"QR code generated successfully and saved to {filename}!")
    except Exception as e:
        print(f"Error generating QR code: {e}")

def main():
    # UPI Payment URL
    upi_url = 'upi://pay?pa=9849606525@axl"
    
    # Filename to save QR code
    filename = "payment_qr.png"
    
    generate_qr_code(upi_url, filename)

if __name__ == "__main__":
    main()