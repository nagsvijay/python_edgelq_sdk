import os

import subprocess

 

def process_proto_files(input_dir, output_parent_dir,google_dir,goten_dir,watchdog_dir):

   

    # Normalize the input and output directory paths

    input_dir = os.path.normpath(input_dir)

    output_parent_dir = os.path.normpath(output_parent_dir)

    google_directory = os.path.normpath(google_dir)

    goten_directory = os.path.normpath(goten_dir)

    watchdog_directory = os.path.normpath(watchdog_dir)

 

    #itr_dir = os.path.normpath(iteration_directory)

 

    # Walk through the directory structure

    for root, dirs, files in os.walk(input_dir):

        for file in files:

            if file.endswith('.proto'):

                # Define the full path to the .proto file

                proto_file = os.path.join(root, file)

               

                # Create the corresponding output directory structure

                #relative_path = os.path.relpath(root, input_dir)

                #print("Relative Path", proto_file)

                #output_dir = os.path.join(output_parent_dir, relative_path)

                os.makedirs(output_parent_dir, exist_ok=True)

 

                # Construct the protoc command with multiple proto paths

                proto_paths = [f'--proto_path={input_dir}'] + [f'--proto_path={goten_directory}'] + [f'--proto_path={google_directory}'] + [f'--proto_path={watchdog_directory}']

                # Run the protoc command with the output directory

                #subprocess.run(['C:/Users/nagarajan12.m/OneDrive - NTT Ltd/Solution Architecture/Spectra Edge Platform Productization/Cutle Query Response JSON/protoc-29.0-rc-1-win64/bin/protoc', f'--python_out={output_dir}', proto_file])

                #print("Input Directory", proto_paths)

                #print("Output Directory", output_dir)

                print("Proto File", proto_file)

                protoc_path = 'C:/Users/nagsv/EdgePlatform/protoc-28.2-win64/bin/protoc.exe'

                #subprocess.run(['C:/Users/nagarajan12.m/OneDrive - NTT Ltd/Solution Architecture/Spectra Edge Platform Productization/Cutle Query Response JSON/protoc-29.0-rc-1-win64/bin/protoc.exe', f'--proto_path={proto_paths}', f'--python_out={output_dir}', proto_file])

                command = [protoc_path] + proto_paths + [f'--python_out={output_parent_dir}', f'--grpc_python_out={output_parent_dir}', proto_file]

                print("Command", command)
                
                subprocess.run(command)

 

# Define the input directory and output parent directory

input_directory = 'C:/Users/nagsv/EdgePlatform/'

#iteration_directory = 'C:/Users/nagsv/EdgePlatform/edgelq-sdk'

output_parent_directory = 'C:/Users/nagsv/EdgePlatform/edgelq_sdk/'

 

# Define additional proto paths

google_directory = 'C:/Users/nagsv/EdgePlatform/googleapis'

goten_directory = 'C:/Users/nagsv/EdgePlatform/goten-sdk/contrib/protobuf'

watchdog_directory = 'C:/Users/nagsv/EdgePlatform/watchdog-sdk'

 

# Process the .proto files

process_proto_files(input_directory, output_parent_directory,google_directory,goten_directory,watchdog_directory)

 

print(f"Processing complete. Generated Python files are saved in the '{output_parent_directory}' directory structure.")

 

 