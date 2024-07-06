import os

def correct_labels(label_path, nc):
    for root, _, files in os.walk(label_path):
        for file in files:
            if file.endswith('.txt'):
                label_file_path = os.path.join(root, file)
                with open(label_file_path, 'r') as f:
                    lines = f.readlines()
                
                corrected_lines = []
                for line in lines:
                    parts = line.split()
                    class_id = int(parts[0])
                    if class_id >= nc:
                        print(f"Correcting {label_file_path}: {class_id}")
                        class_id = nc - 1  # Map to the maximum valid class index
                    parts[0] = str(class_id)
                    corrected_lines.append(" ".join(parts) + "\n")
                
                with open(label_file_path, 'w') as f:
                    f.writelines(corrected_lines)

if __name__ == "__main__":
    dataset_base_path = 'path/to/your/dataset'
    train_label_path = os.path.join(dataset_base_path, 'train/labels')
    val_label_path = os.path.join(dataset_base_path, 'val/labels')
    test_label_path = os.path.join(dataset_base_path, 'test/labels')
    nc = 256  # Number of classes

    print("Correcting training labels...")
    correct_labels(train_label_path, nc)
    
    print("Correcting validation labels...")
    correct_labels(val_label_path, nc)
    
    print("Correcting test labels...")
    correct_labels(test_label_path, nc)

    print("Label correction complete.")
