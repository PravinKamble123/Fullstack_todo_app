<template>
  <div class="home">
    <h1 class="title">Vuengo</h1>

    <hr>

    <div class="columns">
      <div class="column is-4 is-offset-3">
        <form v-on:submit.prevent="addTask()">
          <h2 class="subtitle">Add task</h2>
          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <input class="input" type="text" v-model="description">
            </div>
          </div>
          <div class="field">
            <label class="label">Status</label>
            <div class="control">
              <div class="select is-rounded is-primary" >
                <select v-model="status">
                  <option value="todo">Todo</option>
                  <option value="done">done</option>
                  
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <div class="columns">
      <div class="column is-6">
        <h2 class="subtitle">
          Todo
        </h2>
        <div class="todo-list">
          <div class="card" v-for="task in tasks" :key="task.id" 
                            >
              
            <div class="card-content" v-if="task.status === 'todo'">
              <p class="task-desc">{{ task.description }}</p>
            </div>
            
            <footer class="card-footer" v-if="task.status === 'todo'" >
              <a class="card-footer-item button is-success is-outlined mt-4" @click="setStatus(task.id,'done')">
                Done
              </a>
              <a class="card-footer-item button is-danger is-outlined mt-4" @click="deleteTask(task.id)">
                delete
              </a>
            </footer>
          </div>
        </div>
      </div>

      <div class="column is-6">
        <h2 class="subtitle">Done</h2>
        <div class="done-list">
          <div class="card" v-for="task in tasks" :key="task.id">
            <div class="card-content" v-if="task.status === 'done'">
              <p class="task-desc">{{ task.description }}</p>
            </div>
            <footer class="card-footer" v-if="task.status === 'done'">
              <a class="card-footer-item button is-success is-outlined mt-4" @click="setStatus(task.id,'todo')">
                To do
              </a>
              <a class="card-footer-item button is-danger is-outlined mt-4" @click="deleteTask(task.id)">
                delete
              </a>
            </footer>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      tasks: [],
      description:'',
      status:'todo',
    }
  },
  
  mounted() {
    this.getTasks();
  },
  methods: {
    getTasks() {
      axios({
        method: 'get',
        url: 'http://localhost:8000/api/v1/tasks/task/',
        auth: {
          username: 'admin',
          password: 'root',
        }
      }).then(response => {
        console.log(response.data)
        this.tasks = response.data;
      })
    },
    addTask(){
      if(this.description){
        axios({
          method:'post',
          url: 'http://localhost:8000/api/v1/tasks/task/',
          data:{
            description: this.description,
            status: this.status
          },
          auth: {
            username: 'admin',
            password: 'root',
          }
        }).then(response => {
          let newTask ={
            'id': response.data.id,
            'status': response.data.status,
            'description': response.data.description
          }

          this.tasks.push(newTask)

          this.description = '';
          this.status ='todo';
        })
      }
    },
    setStatus(task_id, status) {
    
      console.log(task_id)
      const task= this.tasks.filter(task => task.id === task_id)[0]
      const description= task.description

      axios({
        method:'put',
        url:'http://localhost:8000/api/v1/tasks/task/'+ task_id + '/',
        headers: {
          'Content-Type':'application/json',
        },
        data:{
          status: status,
          description:description

        },
        
        auth: {
          username: 'admin',
          password: 'root',
        }

      }).then(() =>{
        task.status= status
      })
    },
    deleteTask(taskId) {
    axios({
      method: 'delete',
      url: `http://localhost:8000/api/v1/tasks/task/${taskId}`,
      auth: {
        username: 'admin',
        password: 'root',
      },
    }).then(() => {
      this.tasks = this.tasks.filter((task) => task.id !== taskId);
    });
  },
  }
}
</script>



<style lang="scss">
.home {
  padding: 20px;
  background-color: #f5f5f5;
}

.title {
  font-size: 3rem;
  margin-bottom: 20px;
  color: #007aff;
}

.subtitle {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

hr {
  margin-bottom: 20px;
  border-top: 1px solid #dbdbdb;
}

.field {
  margin-bottom: 20px;
}

.task-desc {
  font-size: 1.2rem;
  margin-bottom: 0;
}

.select, select {
  width: 100%;
  height: 2.5rem;
}

.is-rounded {
  border-radius: 20px;
}

.is-primary {
  border-color: #007aff;
}

.button {
  border-radius: 20px;
}

.is-link {
  background-color: #007aff;
}

.is-success {
  background-color: #00d1b2;
}

.is-outlined {
  border-color: #00d1b2;
  color: #00d1b2;
}

.card {
  background-color: #fff;
  box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
  margin-bottom: 1rem;
  transition: box-shadow 0.2s ease-in-out;

  &:hover {
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.2);
  }

  .card-content {
    padding: 1rem;
  }

  .card-footer {
    padding: 0.5rem;
    display: flex;
    justify-content: flex-end;

    .card-footer-item {
      margin-left: 1rem;
    }
  }
}

.done {
  opacity: 0.5;
}

.is-link {
  background-color: #209cee;
  color: #fff;
}

.select, select {
  width: 100%;
}

input[type="text"] {
  border: none;
  border-bottom: 1px solid #dbdbdb;
  padding: 0.5rem;
  font-size: 1rem;
  margin-bottom: 1rem;

  &:focus {
    outline: none;
    border-color: #3273dc;
  }
}

button {
  border: none;
  border-radius: 5px;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;

  &:focus {
    outline: none;
  }

  &:hover {
    background-color: #3273dc;
  }
}

@media screen and (max-width: 768px) {
  .column {
    margin-top: 2rem;
  }

  .columns {
    margin-top: 0;
  }
}
</style>




