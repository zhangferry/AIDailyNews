<script lang="ts">
  import { onMount } from "svelte";
  import "gitalk/dist/gitalk.css";
  import Gitalk from "gitalk";

  onMount(() => {
    const gitalk = new Gitalk({
      clientID: import.meta.env.PUBLIC_GITTALK_CLIENT_ID,
      clientSecret: import.meta.env.PUBLIC_GITTALK_CLIENT_SECRET,
      repo: import.meta.env.PUBLIC_GITTALK_REPO, // The repository of store comments,
      owner: import.meta.env.PUBLIC_GITTALK_OWNER,
      admin: [import.meta.env.PUBLIC_GITTALK_OWNER],
      id: location.pathname, // Ensure uniqueness and length less than 50
      distractionFreeMode: false, // Facebook-like distraction free mode
    });
    gitalk.render("gitalk-container");
  });
</script>

<div id="gitalk-container"></div>
