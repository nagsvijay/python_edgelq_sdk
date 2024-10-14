import os

import subprocess

import traceback

 

# Define the root directory containing your .proto files

input_directory = 'C:/Users/nagsv/EdgePlatform/'

#input_directory = 'C:/Users/nagsv/EdgePlatform/watchdog_sdk'

output_directory = 'C:/Users/nagsv/EdgePlatform/edgelq_sdk'

goten_directory = 'C:/Users/nagsv/EdgePlatform/goten-sdk/contrib/protobuf'

def process_proto_files(in_dir, out_dir,got_dir):

    # Walk through the directory tree

    # Normalize the input and output directory paths

    input_dir = os.path.normpath(in_dir)

    output_dir = os.path.normpath(out_dir)

    goten_dir = os.path.normpath(got_dir)
    
    try:

        for subdir, dirs, files in os.walk(input_dir):

            print("Sub Dir -",subdir)

            for file in files:

                if file.endswith('.proto'):

                    proto_file = os.path.join(subdir, file)

                    '''print("Dir Name -",dirs)

                    print("Output Dir",output_dir)

                    pyout_dir = os.path.join(output_dir,dirs)

                    print("Required Path -",pyout_dir)

                    print("ProtoFile Name -",proto_file)'''

                    # Calculate the relative path from the input root directory

                    #relative_path = os.path.relpath(subdir, input_dir)

                    # Create the corresponding output directory

                    #pyout_dir = os.path.join(output_dir, relative_path)

                    os.makedirs(output_dir, exist_ok=True)

                    '''print("Required Path -",output_dir)
                    print("Required Path -",input_dir)
                    print("Required Path -",goten_dir)'''

                    # Run the protoc command

                    subprocess.run([

                        'python', '-m', 'grpc_tools.protoc',

                        f'--proto_path={input_dir}',
                        
                        f'--proto_path={goten_dir}',

                        f'--python_out={output_dir}',

                        f'--pyi_out={output_dir}',

                        f'--grpc_python_out={output_dir}',

                        proto_file

                    ])

    except Exception as e:

        traceback.print_exc()

        return False

   

 

# Process the .proto files

process_proto_files(input_directory, output_directory, goten_directory)

 

print(f"Processing complete. Generated Python files are saved in the '{input_directory}' directory structure.")

 

 