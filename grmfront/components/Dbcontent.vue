<template>
    <div>
        <b-container fluid>
    <b-row>
        <b-col cols="5">
            <tr>
                <h1>Alerts</h1>
            </tr>
            <table class="rux-table">
                <tr class="rux-table__column-head">
                    <th>Message</th>
                    <th>Category</th>
                    <th>Time</th>
                </tr>
                <tr v-for="alert in alerts" :key="alert"><td>{{ alert['errorMessage'] }}</td><td>{{ alert['errorCategory'] }}</td><td>{{ alert['errorTime'] }}</td></tr>
            </table>
        </b-col>
        <b-col cols="7">
            <tr>
                <h1>Contacts</h1>
            </tr>
            <table class="rux-table">
                <tr class="rux-table__column-head">
                    <th>Name</th>
                    <th>Status</th>
                    <th>Begin Timestamp</th>
                    <th>End Timestamp</th>
                </tr>
                <tr v-for="contact in contacts" :key="contact"><td>{{ contact['contactName'] }}</td><td>{{ contact['contactStatus'] }}</td><td>{{ contact['contactBeginTimestamp'] }}</td><td>{{ contact['contactEndTimestamp'] }}</td></tr>
            </table>
        </b-col>
        </b-row>
    </b-container>
    </div>
</template>


<script>
import { RuxGlobalStatusBar } from '@astrouxds/rux-global-status-bar/rux-global-status-bar.js'
import { RuxIcon } from '@astrouxds/rux-icon/rux-icon.js';

export default {
  name: 'Dbcontent',
  data() {
      return{
          alerts: {},
          contacts: {},
          user: {}
      }
  },
  head() {
      return {
          bodyAttrs: {
              class: "dark-theme"
          }
      }
  },
  methods: {
      processAlerts(data){
          this.alerts = data['alerts']
      },
      processContacts(data){
          this.contacts = data['contacts']
      },
      errorNotify(){

      }
  },
  mounted(){
      try{
                const fetchbody = {
                    method: "POST",
                    headers: {
                        'Content-Type': 'Application/json',
                        'authtoken': window.localStorage.getItem("authtoken")},
                    body:  JSON.stringify({status: "get"})
                    }
                fetch('/getalerts', fetchbody).then((response) => response.json()).then(
                    data => (
                        this.processAlerts(data)
                    )
                ).catch(error => 
                    this.errorNotify()
                );
                }
                catch(e) {
                    this.errorNotify()
                }
        try{
            const fetchbody = {
                method: "POST",
                headers: {
                    'Content-Type': 'Application/json',
                    'authtoken': window.localStorage.getItem("authtoken")},
                body:  JSON.stringify({status: "get"})
                }
            fetch('/getcontacts', fetchbody).then((response) => response.json()).then(
                data => (
                    this.processContacts(data)
                )
            ).catch(error => 
                this.errorNotify()
            );
            }
            catch(e) {
                this.errorNotify()
            }
  }
}
</script>

<style scoped>

</style>