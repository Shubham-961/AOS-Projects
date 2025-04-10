import random

def generate_page_references(num_references, num_pages):
    """
    Generate a list of random page references.
    
    :param num_references: Number of page references to generate
    :param num_pages: Total number of unique pages
    :return: List of random page references
    """
    return [random.randint(0, num_pages - 1) for _ in range(num_references)]

def fifo_page_replacement(page_references, frame_size):
    """
    Implement the FIFO (First-In-First-Out) page replacement algorithm.
    
    :param page_references: List of page references
    :param frame_size: Size of the memory frame
    :return: Total number of page faults
    """
    memory = []
    page_faults = 0

    for page in page_references:
        if page not in memory:
            if len(memory) >= frame_size:
                memory.pop(0)  # Remove the oldest page (first in)
            memory.append(page)  # Add the new page
            page_faults += 1
    
    return page_faults

def main():
    # Set simulation parameters
    num_references = 100
    num_pages = 20
    frame_size = 5

    # Generate random page references
    page_references = generate_page_references(num_references, num_pages)

    # Run FIFO algorithm
    total_faults = fifo_page_replacement(page_references, frame_size)

    # Print results
    print(f"Number of page references: {num_references}")
    print(f"Number of unique pages: {num_pages}")
    print(f"Frame size: {frame_size}")
    print(f"Total page faults: {total_faults}")

if __name__ == "__main__":
    main()
