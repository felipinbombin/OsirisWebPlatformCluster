#!/bin/bash

#SBATCH --job-name=speed
#SBATCH --partition=slims
#SBATCH -n 1
#SBATCH --output=osiris/logs/archivo_%j.out
#SBATCH --error=osiris/logs/archivo_%j.err
##SBATCH --mail-user=usuario@gmail.com
##SBATCH --mail-type=ALL

module load python/3.5.2

#
# REMOTE PARAMETERS
#
REMOTE_USER="server"
OSIRIS_WEB_IP=$1
REMOTE_RESPONSE_PYTHON_FILE=$2
REMOTE_PYTHON_COMMAND=$3
EXECUTION_ID=$4
MODEL_INPUT_FILE_NAME=$5
REMOTE_MODEL_NAME=$6
REMOTE_MODEL_OUTPUT_PATH=$7
#
# LOCAL PARAMETER
#
SSH_PATH=~/.ssh
OSIRIS_PATH=~/osiris
OUTPUT_PATH="$OSIRIS_PATH"/outputs
INPUT_PATH="$OSIRIS_PATH"/inputs
MODEL_OUTPUT="$EXECUTION_ID.output"

echo "OSIRIS_WEB_IP: $OSIRIS_WEB_IP"
echo "REMOTE_RESPONSE_PYTHON_FILE: $REMOTE_RESPONSE_PYTHON_FILE"
echo "REMOTE_PYTHON_COMMAND: $REMOTE_PYTHON_COMMAND"
echo "EXECUTION_ID: $EXECUTION_ID"
echo "MODEL_INPUT_FILE_NAME: $MODEL_INPUT_FILE_NAME"
echo "REMOTE_MODEL_NAME: $REMOTE_MODEL_NAME"
echo "REMOTE_MODEL_OUTPUT_PATH: $REMOTE_MODEL_OUTPUT_PATH"

# save stderr output and std output in variables
ERR_LOG=$((
(
python3 "$OSIRIS_PATH"/runModel.py "$REMOTE_MODEL_NAME" "$INPUT_PATH/$MODEL_INPUT_FILE_NAME" "$OUTPUT_PATH/$MODEL_OUTPUT"
) 1>"$OSIRIS_PATH/$EXECUTION_ID"
) 2>&1)
OUT_LOG=$(<"$OSIRIS_PATH/$EXECUTION_ID")

echo "$OUT_LOG"
echo "$ERR_LOG"

# move answer file
scp -i "$SSH_PATH"/id_rsa "$OUTPUT_PATH/$MODEL_OUTPUT" "$REMOTE_USER"@"$OSIRIS_WEB_IP":"$REMOTE_MODEL_OUTPUT_PATH"/"$MODEL_OUTPUT"
# save model answer
ssh -i "$SSH_PATH"/id_rsa "$REMOTE_USER"@"$OSIRIS_WEB_IP" "$REMOTE_PYTHON_COMMAND $REMOTE_RESPONSE_PYTHON_FILE $EXECUTION_ID $MODEL_OUTPUT \"$OUT_LOG\" \"$ERR_LOG\""

# delete temp file
rm "$OSIRIS_PATH/$EXECUTION_ID"
#rm "$OUTPUT_PATH/$MODEL_OUTPUT"
#rm "$INPUT_PATH/$MODEL_INPUT_FILE_NAME"
