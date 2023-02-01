# cap-sample-data
Sample data archive for use with the clean-air-project.

## Updating local Conda package after changes
When a change is made in this repository, users will need to update their local version to reflect this. For code running in the `cap_env` Conda environment, the following terminal commands should work:

1. Activate the environment if you haven't already: 
`conda activate cap_env`
2. `pip uninstall cap_sample_data`
3. Update the environment from the yaml file: 
`conda env update --file environment.yml --prune`