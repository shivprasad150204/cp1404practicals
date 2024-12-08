from project import Project

def load_projects(filename="projects.txt"):
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            name, start_date, priority, cost, completion = line.strip().split('\t')
            projects.append(Project(name, start_date, priority, cost, completion))
    return projects

def display_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        if not project.is_completed():
            print(project)
    print("\nCompleted projects:")
    for project in projects:
        if project.is_completed():
            print(project)

def main():
    projects = load_projects()
    display_projects(projects)

if __name__ == "__main__":
    main()
