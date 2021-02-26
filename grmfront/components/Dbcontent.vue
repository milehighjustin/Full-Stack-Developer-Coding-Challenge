<template>
    <div>
        <b-container>
    <b-row>
        <b-col style="width: 100%;" sm>
            <rux-global-status-bar>
                <h1>Alerts</h1>
            </rux-global-status-bar>
            <table class="rux-table">
                <tr class="rux-table__column-head">
                    <th>Message</th>
                    <th>Category</th>
                    <th>Time</th>
                </tr>
                <tr>
                    <td>Name</td>
                    <td>Status</td>
                    <td>Begin Timestamp</td>
                </tr>
            </table>
        </b-col>
        <b-col sm>
            <rux-global-status-bar>
                <h1>Contacts</h1>
            </rux-global-status-bar>
            <table class="rux-table">
                <tr class="rux-table__column-head">
                    <th>Name</th>
                    <th>Status</th>
                    <th>Begin Timestamp</th>
                    <th>End Timestamp</th>
                </tr>
                <tr>
                    <td>Name</td>
                    <td>Status</td>
                    <td>Begin Timestamp</td>
                    <td>End Timestamp</td>
                </tr>
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
  head() {
      return {
          bodyAttrs: {
              class: "dark-theme"
          }
      }
  }
}
</script>

<style scoped>

</style>