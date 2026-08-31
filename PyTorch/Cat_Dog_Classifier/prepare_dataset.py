from pathlib import Path
import shutil


# Where your downloaded dataset is
SOURCE = Path(r"C:\Users\Saruk meeya\Downloads\archive")

# Where our small dataset will be created
DESTINATION = Path(__file__).resolve().parent / "datasets"

TRAIN_COUNT = 400
TEST_COUNT = 100


def find_folder(parent, possible_names):
    """Find a folder by trying several possible names."""
    for name in possible_names:
        folder = parent / name
        if folder.exists():
            return folder

    return None


def copy_images(source_folder, destination_folder, count):

    if source_folder is None:
        print("ERROR: Source folder not found.")
        return

    destination_folder.mkdir(parents=True, exist_ok=True)

    # Accept jpg, jpeg and png
    images = []

    for extension in ["*.jpg", "*.jpeg", "*.png"]:
        images.extend(source_folder.glob(extension))

    images = images[:count]

    for image in images:
        shutil.copy2(image, destination_folder / image.name)

    print(f"Copied {len(images)} images → {destination_folder}")


# Check that SOURCE actually exists
if not SOURCE.exists():
    print(f"ERROR: Dataset folder not found:")
    print(SOURCE)
    exit()


print("Dataset location found:")
print(SOURCE)
print()


# Show what's actually inside achieve
print("Folders inside achieve:")

for item in SOURCE.rglob("*"):
    if item.is_dir():
        print(" ", item)

print()


# Find train and test folders
train_folder = find_folder(SOURCE, ["train", "Train", "TRAIN"])
test_folder = find_folder(SOURCE, ["test", "Test", "TEST"])


if train_folder is None:
    print("ERROR: Could not find the train folder.")
    exit()

if test_folder is None:
    print("ERROR: Could not find the test folder.")
    exit()


# Find cat/dog folders
train_cats = find_folder(train_folder, ["cats", "cat", "Cats", "Cat"])
train_dogs = find_folder(train_folder, ["dogs", "dog", "Dogs", "Dog"])

test_cats = find_folder(test_folder, ["cats", "cat", "Cats", "Cat"])
test_dogs = find_folder(test_folder, ["dogs", "dog", "Dogs", "Dog"])


print("Detected folders:")
print("Train cats:", train_cats)
print("Train dogs:", train_dogs)
print("Test cats :", test_cats)
print("Test dogs :", test_dogs)
print()


# Copy images
copy_images(
    train_cats,
    DESTINATION / "train" / "cats",
    TRAIN_COUNT
)

copy_images(
    train_dogs,
    DESTINATION / "train" / "dogs",
    TRAIN_COUNT
)

copy_images(
    test_cats,
    DESTINATION / "test" / "cats",
    TEST_COUNT
)

copy_images(
    test_dogs,
    DESTINATION / "test" / "dogs",
    TEST_COUNT
)


print()
print("Dataset preparation complete! 🚀")