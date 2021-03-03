<script>
  export let projectUrl;
  export let projectPicUrl;
  export let projectName;
  export let projectTech;
  export let projectDescription;
  export let reverse;
</script>

<div class="row" class:flex-row-reverse={reverse}>
  <div class="col-sm  d-flex justify-content-center align-items-center blue pt-4 pb-4">
    <div class="text-center">
      <a class="projectName" href={projectUrl}>{projectName}</a><br />
      {projectDescription}
      <br /> Made with: {projectTech}
    </div>
  </div>
  <div class="col-sm white">
    <img width="100%" alt src={projectPicUrl} />
  </div>
</div>

<style>
  .projectName {
    font-size: 1.4em;
  }

  .blue {
    background-color: #252657;
  }

  .white {
    background-color: rgb(252, 244, 231);
  }
</style>
