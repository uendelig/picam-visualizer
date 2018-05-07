<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <v-btn color="primary" dark @click.stop="dialog = true">Camera 1</v-btn>
    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition" scrollable >
          <v-card tile>
            <v-toolbar card dark color="primary">
              <v-btn icon @click.native="dialog = false" dark>
                <v-icon>close</v-icon>
              </v-btn>
              <v-toolbar-title>Camera 1</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>

            <div class="cam-menu-content">
              <div class="preview">
                <v-icon x-large color="white">visibility_off</v-icon>
              </div>
              <div>
                <v-btn outline fab color="green" v-on:click="play">
                  <v-icon>play_arrow</v-icon>
                </v-btn>
                <v-btn outline fab color="red" v-on:click="stop">
                  <v-icon>stop</v-icon>
                </v-btn>
              </div>
            </div>

            <div style="flex: 1 1 auto;"></div>
          </v-card>
        </v-dialog>
  </div>
</template>

<script>

var totalSecondes = 0;
var timer;
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Picam-Visualizer',
      time: {
        min: 0,
        sec: 0
      },
      dialog: false
    }
  },
  methods: {
    play: function() {
	fetch("http://192.168.0.26:5000/start");
    },
    stop: function() {
	fetch("http://192.168.0.26:5000/stop");
    }
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.preview {
  min-height: 500px;
  min-width: 500px;
  margin: auto;
  border-style: solid;
  border-color: white;
  display: -webkit-flex;
  -webkit-flex-wrap: wrap;
  flex-wrap: wrap;
  -webkit-align-content: center;
  align-content: center;
}

.cam-menu-content {
  padding-top: 1%;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
