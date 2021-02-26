<template>
<div>
<rux-global-status-bar>
    <h1><rux-icon color="#fff" icon="satellite-transmit"></rux-icon> GRM Dashboard</h1>
</rux-global-status-bar>
<slot></slot>
</div>
</template>

<script>
import { RuxGlobalStatusBar } from '@astrouxds/rux-global-status-bar/rux-global-status-bar.js'
import { RuxIcon } from '@astrouxds/rux-icon/rux-icon.js';

export default {
  name: 'AppLayout',
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
.rux-table {
    
}
</style>


