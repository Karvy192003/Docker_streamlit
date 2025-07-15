
import streamlit as st
import subprocess

st.title("Docker Manager")

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr
    except:
        return "", "Error running command"

st.sidebar.header("Choose What To Do")
option = st.sidebar.selectbox("Pick One:", [
    "List Containers", 
    "Start Container", 
    "Run Container",
    "Stop Container", 
    "Remove Container",
    "List Images",
    "Pull Image",
    "Remove Image",
    "List Networks",
    "Create Network",
    "Remove Network",
    "List Volumes",
    "Create Volume", 
    "Remove Volume",
    "System Cleanup"
])

if option == "List Containers":
    st.header("All Containers")
    if st.button("Show Containers"):
        output, error = run_command("docker ps -a")
        if output:
            st.text(output)
        if error:
            st.error(error)

elif option == "Start Container":
    st.header("Start a Container")
    run_command(f"docker ps -a")
    container_name = st.text_input("Enter container name or ID:")
    if st.button("Start"):
        if container_name:
            output, error = run_command(f"docker start {container_name}")
            if output:
                st.success(f"Started {container_name}")
                st.text(output)
            if error:
                st.error(error)

elif option == "Stop Container":
    st.header("Stop a Container")
    container_name = st.text_input("Enter container name or ID:")
    if st.button("Stop"):
        if container_name:
            output, error = run_command(f"docker stop {container_name}")
            if output:
                st.success(f"Stopped {container_name}")
                st.text(output)
            if error:
                st.error(error)


elif option == "Remove Container":
    st.header("Remove a Container")
    container_name = st.text_input("Enter container name or ID:")
    if st.button("Remove"):
        if container_name:
            output, error = run_command(f"docker rm {container_name}")
            if output:
                st.success(f"Removed {container_name}")
                st.text(output)
            if error:
                st.error(error)

elif option == "List Images":
    st.header("All Images")
    if st.button("Show Images"):
        output, error = run_command("docker images")
        if output:
            st.text(output)
        if error:
            st.error(error)

elif option == "Pull Image":
    st.header("Pull an Image")
    image_name = st.text_input("Enter image name (like nginx, ubuntu):")
    if st.button("Pull"):
        if image_name:
            st.info("Pulling image... please wait")
            output, error = run_command(f"docker pull {image_name}")
            if "Downloaded" in output or "up to date" in output:
                st.success(f"Got {image_name}")
            st.text(output)
            if error:
                st.error(error)

elif option == "Remove Image":
    st.header("Remove an Image")
    image_name = st.text_input("Enter image name or ID:")
    if st.button("Remove"):
        if image_name:
            output, error = run_command(f"docker rmi {image_name}")
            if output:
                st.success(f"Removed {image_name}")
                st.text(output)
            if error:
                st.error(error)

elif option == "List Networks":
    st.header("All Networks")
    if st.button("Show Networks"):
        output, error = run_command("docker network ls")
        if output:
            st.text(output)
        if error:
            st.error(error)

elif option == "Create Network":
    st.header("Create a Network")
    network_name = st.text_input("Enter network name:")
    if st.button("Create"):
        if network_name:
            output, error = run_command(f"sudo docker network create {network_name}")
            if output:
                st.success(f"Created network {network_name}")
                st.text(output)
            if error:
                st.error(error)

elif option == "Remove Network":
    st.header("Remove a Network")
    network_name = st.text_input("Enter network name:")
    if st.button("Remove"):
        if network_name:
            output, error = run_command(f"sudo docker network rm {network_name}")
            if output:
                st.success(f"Removed network {network_name}")
                st.text(output)
            if error:
                st.error(error)

elif option == "List Volumes":
    st.header("All Volumes")
    if st.button("Show Volumes"):
        output, error = run_command("sudo docker volume ls")
        if output:
            st.text(output)
        if error:
            st.error(error)

elif option == "Create Volume":
    st.header("Create a Volume")
    volume_name = st.text_input("Enter volume name:")
    if st.button("Create"):
        if volume_name:
            output, error = run_command(f"sudo docker volume create {volume_name}")
            if output:
                st.success(f"Created volume {volume_name}")
                st.text(output)
            if error:
                st.error(error)

elif option == "Remove Volume":
    st.header("Remove a Volume")
    volume_name = st.text_input("Enter volume name:")
    if st.button("Remove"):
        if volume_name:
            output, error = run_command(f"sudo docker volume rm {volume_name}")
            if output:
                st.success(f"Removed volume {volume_name}")
                st.text(output)
            if error:
                st.error(error)

elif option == "System Cleanup":
    st.header("Clean Up Docker")
    st.write("This will remove unused stuff to free up space")
    if st.button("Clean Up"):
        st.info("Cleaning... please wait")
        output, error = run_command("sudo docker system prune -f")
        if output:
            st.success("Cleanup done!")
            st.text(output)
        if error:
            st.error(error)

st.write("---")
st.write("Made with Streamlit")
