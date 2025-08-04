document.addEventListener("DOMContentLoaded", () => {
    const taskInput = document.getElementById("task-text");
    const addTaskBtn = document.getElementById("add-task-btn");
    const taskList = document.getElementById("task-list");

    const API_BASE_URL = "http://127.0.0.1:8000";

    async function fetchTasks() {
        try {
            const response = await fetch(`${API_BASE_URL}/tasks`);
            if (!response.ok) {
                throw new Error("Failed to fetch tasks");
            }
            const tasks = await response.json();
            taskList.innerHTML = "";
            tasks.forEach(task => {
                const li = document.createElement("li");
                li.innerHTML = `
                    <span>${task.text}</span>
                    <div>
                        <button class="edit-btn" data-id="${task.id}" data-text="${task.text}">Edit</button>
                        <button class="delete-btn" data-id="${task.id}">X</button>
                    </div>
                `;
                taskList.appendChild(li);
            });

            document.querySelectorAll(".delete-btn").forEach(button => {
                button.addEventListener("click", async (event) => {
                    const taskId = event.target.dataset.id;
                    await deleteTask(taskId);
                });
            });

            document.querySelectorAll(".edit-btn").forEach(button => {
                button.addEventListener("click", async (event) => {
                    const taskId = event.target.dataset.id;
                    const taskText = event.target.dataset.text;
                    const newText = prompt("Edit your task:", taskText);
                    if (newText !== null && newText.trim() !== "") {
                        await updateTask(taskId, newText);
                    }
                });
            });
        } catch (error) {
            console.error("Error fetching tasks:", error);
        }
    }

    async function addTask() {
        const taskText = taskInput.value.trim();
        if (taskText !== "") {
            try {
                const response = await fetch(`${API_BASE_URL}/tasks`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ text: taskText }),
                });
                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.detail || "Failed to add task");
                }
                fetchTasks();
                taskInput.value = "";
            } catch (error) {
                console.error("Error adding task:", error);
            }
        }
    }

    async function deleteTask(taskId) {
        try {
            const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
                mode: "cors",
            });
            if (!response.ok) {
                throw new Error("Failed to delete task");
            }
            fetchTasks();
        } catch (error) {
            console.error("Error deleting task:", error);
        }
    }

    async function updateTask(taskId, newText) {
        try {
            const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id: taskId,
                    text: newText,
                    is_completed: false,
                }),
            });
            if (!response.ok) {
                throw new Error("Failed to update task");
            }
            fetchTasks();
        } catch (error) {
            console.error("Error updating task:", error);
        }
    }

    addTaskBtn.addEventListener("click", addTask);
    fetchTasks();
});
