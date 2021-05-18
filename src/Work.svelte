<script>
  import Project from './Project.svelte';
</script>

<div id="projects">
  <Project
    projectName={'avtosijaj.si'}
    projectUrl={'https://avtosijaj.si'}
    projectDescription={'Portfolio website for car polishing company'}
    projectTech={'Vue.js'}
    projectPicUrl={'./assets/avtosijaj.jpg'}
    reverse={false}
  />

  <Project
    projectName={'3dprintedsound.com'}
    projectUrl={'https://3dprintedsound.com'}
    projectDescription={'Website that can generate 3D(*.stl) waveform out of sound.'}
    projectTech={'Vannila JS, THREE.js library'}
    projectPicUrl={'./assets/3dprintedsound.jpg'}
    reverse={true}
  />

  <Project
    projectName={'github.com/timtoplak/ttab'}
    projectUrl={'https://github.com/timtoplak/ttab'}
    projectDescription={'New tab override'}
    projectTech={'Vue.js'}
    projectPicUrl={'./assets/ttab.jpg'}
    reverse={false}
  />
</div>

<style>
</style>
