def modify_file_content(content):
   
    return content.upper()


def main():
    try:
       
        input_filename = input("Enter the filename to read: ")

        
        with open(input_filename, "r") as infile:
            content = infile.read()

        modified_content = modify_file_content(content)

        output_filename = "modified_" + input_filename

        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File successfully modified and saved as '{output_filename}'")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f" Unexpected error: {e}")


if __name__ == "__main__":
    main()
