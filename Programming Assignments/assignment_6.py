import os

# Global storage for the matrix
GLOBAL_MATRIX = None


def get_matrix(filename: str = None) -> list:
    global GLOBAL_MATRIX
    while True:
        try:
            filename = input("Enter the matrix filename (should include extension if there is one): ").strip()

            filepath = os.path.join("text_files", filename)

            with open(filepath, "r") as f:
                rows = [list(map(int, line.strip().split())) for line in f if line.strip()]

            GLOBAL_MATRIX = [list(col) for col in zip(*rows)]

            print("it worked yay")
            for col in GLOBAL_MATRIX:
                print(col)

            return GLOBAL_MATRIX

        except FileNotFoundError:
            print(f"file '{filename}' not found in 'text_files' directory. try again, maybe you forgot extension or included full directory (just the file name).")
            filename = None
        except ValueError:
            print("file contains non-integer values. ensure all entries are integers (not floats).")
            filename = None
        except Exception as e:
            print(f" Unexpected error: {e}")
            filename = None

def write_matrix(filename: str = None, matrix: list = None, adjustment: int = None, *row_numbers: int) -> bool:
    try:
        filename = input("Enter the filename to save the adjusted matrix : ").strip()
        filepath = os.path.join("text_files", filename)

        if matrix is None:
            if GLOBAL_MATRIX is None:
                print("No matrix loaded globally. Run get_matrix() first.")
                return False
            matrix = GLOBAL_MATRIX

        if adjustment is None:
            adjustment = int(input("Enter the adjustment multiplier (integer): ").strip())

        if not row_numbers:
            row_input = input("Enter row numbers separated by spaces (or press Enter for all rows): ").strip()
            if row_input:
                row_numbers = list(map(int, row_input.split()))
            else:
                row_numbers = range(len(matrix[0]))  # all rows

        adjusted_matrix = [col[:] for col in matrix]

        # Apply adjustment
        for col in adjusted_matrix:
            for r in row_numbers:
                col[r] *= adjustment

        # Convert back to row-major for writing
        rows = zip(*adjusted_matrix)

        # Check if file exists
        if os.path.exists(filepath):
            confirm = input(f"File '{filename}' already exists. Overwrite? (y/n): ").strip().lower()
            if confirm != "y":
                print("Write cancelled. File not overwritten.")
                return False

        # Write to file
        with open(filepath, "w") as f:
            for row in rows:
                f.write(" ".join(map(str, row)) + "\n")

        print(f"Matrix written to '{filename}' successfully.")
        return True

    except Exception as e:
        print(f"Error writing matrix: {e}")
        return False
