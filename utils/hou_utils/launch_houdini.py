def setup_env(self):
        env_file = "C:/Users/PERMAN/Documents/houdini18.5/houdini.env"
        search_text = "# Glacier Variables"
        num_var = 6
        
        #Cleanup the file
       # Read the file content into a list of lines
        with open(env_file, 'r') as file:
            lines = file.readlines()

        # Create an empty list to store the modified content
        modified_lines = []

        i = 0
        while i < len(lines):
            line = lines[i]

            if search_text in line:
                # Found the search text, add it to the modified content
                modified_lines.append(line)

                # Skip the next lines_to_delete lines
                for _ in range(num_var):
                    i += 1
            else:
                modified_lines.append(line)

            i += 1

        # Write the modified content back to the file
        with open(env_file, 'w') as file:
            file.writelines(modified_lines)

        # print(f"Deleted {num_var} lines after each occurrence of '{search_text}'.")
