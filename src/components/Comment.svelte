<script lang="ts">
  import { onMount } from "svelte";
  import "gitalk/dist/gitalk.css";
  import Gitalk from "gitalk";

  console.error("on gitalk");
  onMount(() => {
    const gitalk = new Gitalk({
      clientID: "012999c912503aff4cac",
      clientSecret: "fcc9ff4a4ca14d80b38de2548cd1102bf7147c57",
      repo: "AIDailyNews", // The repository of store comments,
      owner: "zhangferry",
      admin: ["zhangferry"],
      id: location.pathname, // Ensure uniqueness and length less than 50
      distractionFreeMode: false, // Facebook-like distraction free mode
    });

    console.error("on mount gitalk");
    gitalk.render("gitalk-container");
  });
</script>

<div id="gitalk-container"></div>
