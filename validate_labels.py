import os

def validate_labels(label_path, nc):
    invalid_files = []
    for root, _, files in os.walk(label_path):
        for file in files:
            if file.endswith('.txt'):
                label_file_path = os.path.join(root, file)
                with open(label_file_path, 'r') as f:
                    lines = f.readlines()
                
                for line in lines:
                    parts = line.split()
                    class_id = int(parts[0])
                    if class_id >= nc:
                        invalid_files.append(label_file_path)
                        print(f"Invalid label found in {label_file_path}: {class_id}")
    return invalid_files

if __name__ == "__main__":
    dataset_base_path = 'path/to/your/dataset'
    train_label_path = os.path.join(dataset_base_path, 'train/labels')
    val_label_path = os.path.join(dataset_base_path, 'val/labels')
    test_label_path = os.path.join(dataset_base_path, 'test/labels')
    nc = 256  # Number of classes, change it.

    print("Validating training labels...")
    invalid_train_labels = validate_labels(train_label_path, nc)
    
    print("Validating validation labels...")
    invalid_val_labels = validate_labels(val_label_path, nc)
    
    print("Validating test labels...")
    invalid_test_labels = validate_labels(test_label_path, nc)

    if not invalid_train_labels and not invalid_val_labels and not invalid_test_labels:
        print("All labels are valid.")
    else:
        print("Some labels are invalid.")
