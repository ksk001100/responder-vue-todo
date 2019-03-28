<template>
  <div class="todo">
    <h2>ToDo App<br>Responder + Vue.js</h2>
    <form class="add-item" @submit.prevent="addTodo">
      <label>TASK</label>
      <input type="text" ref="text" placeholder="input here...">
      <button type="submit" class="addButton">ADD</button>
    </form>
    <div class="todoTable">
      <table>
        <thead>
          <tr>
            <th class="id">ID</th>
            <th class="text">TASK</th>
            <th>ACTION</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="todo in todos" :key="todo.id">
            <td>{{ todo.id }}</td>
            <td>{{ todo.text }}</td>
            <td class="button">
              <button @click="removeTodo(todo)" class="deleteButton">
                DELETE
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import axios from 'axios';

export interface TodoItem {
    id: number;
    text: string;
}

@Component
export default class Todo extends Vue {
    private todos: TodoItem[] = [];

    private created() {
        axios.get('/api/todos')
            .then((resp) => {
                this.todos = resp.data;
            });
    }

    private addTodo() {
        const text = this.$refs.text as HTMLInputElement;
        if (!text.value.length) {
            return;
        }
        this.todos.push({
            id: this.todos.length !== 0 ? this.todos[this.todos.length - 1].id + 1 : 1,
            text: text.value,
        });
        axios.post('/api/todos', {text: text.value});
        text.value = '';
   }

    private removeTodo(todo: TodoItem) {
        const index = this.todos.indexOf(todo);
        this.todos.splice(index, 1);
        axios.delete('/api/todos/' + todo.id);
    }

}
</script>

<style scoped lang="scss">
table {
  // width: 80%;
  margin: 50px auto;
}
form {
  width: 50%;
  margin: auto;
}
label {
  margin: 0 20px;
}
th, td {
  text-align: center;
  width: 300px;
  padding: 10px 0;
}
button {
  border-radius: 30px;
}
.addButton {
  margin: 0 20px;
  height: 30px;
  width: 50px;
  background-color: #64B587;
  color: white;
  font-weight: bold;
}
.deleteButton {
  height: 30px;
  width: 70px;
  background-color: #ED655A;
  color: white;
  font-weight: bold;
}
.todoTable {
  text-align: center;
}
</style>
