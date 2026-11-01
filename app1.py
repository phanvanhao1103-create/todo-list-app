# Danh sách dể lưu công việc 
tasks =[]
def add_task(task_name) :
    """thêm một công việc mới vào danh sách """
    tasks.append(task_name )
    print(f"đã thêm công việc: '{task_name}'")
#---điểm bắt đầu của chương trình---
if __name__ == "__main__":
    print("chào mừng đến ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")