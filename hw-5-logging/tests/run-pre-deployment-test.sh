#!/bin/bash

echo "Running pre-deploy unit tests"
echo "Running intitial test (should pass)"

ansible-playbook tests/pre-deployment.yml -e fabric_model_path=../tests/models/fabric-correct.yml >/dev/null 2>/dev/null

if [ $? -ne 0 ]; then
    echo ".. Initial test failed. Aborting."
    exit 1
fi
echo ".. Initial test OK. Proceeding."

exitstatus=0
for modtest in tests/models/fabric-invalid-*.yml; do
    echo "Running scenario $modtest"
    ansible-playbook tests/pre-deployment.yml -e fabric_model_path=../$modtest >/dev/null 2>/dev/null
    if [ $? -ne 0 ]; then
        echo ".. Failed as expected."
    else
        echo ">>> DID NOT fail."
        exitstatus=1
    fi
done

if [ $exitstatus -ne 0 ]; then
    echo "Test suite failed"
fi

exit $exitstatus
