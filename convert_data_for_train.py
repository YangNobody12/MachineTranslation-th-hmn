import json

def convert_text_to_json(input_file, output_file):
    data_list = []
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        # Process each line and create JSON structure
        for i, line in enumerate(lines, 1):
            # Assuming the line format is: hmong_text | thai_text
            parts = line.strip().split('-')
            if len(parts) == 2:
                hmong_text = parts[0].strip()
                thai_text = parts[1].strip()
                
                data_item = {
                    "id": i,
                    "translation":{
                        "hmn": hmong_text,
                        "th": thai_text,
                    },
                }
                data_list.append(data_item)
        
        # Write to JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)
            
        print(f"Successfully converted {len(data_list)} entries to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "data.txt"  # Your input text file
    output_file = "data.json"  # Your output JSON file
    convert_text_to_json(input_file, output_file)
