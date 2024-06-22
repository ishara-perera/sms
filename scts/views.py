from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from scts.models import Student
from scts.serializers import StudentCreateSerializer, StudentSerializer


# Create your views here.
# @api_view(['POST'])
# def create_student(request):
#     serializer = StudentCreateSerializer(data=request.data)
#     if serializer.is_valid():
#         student = Student.objects.create(**serializer.validated_data)
#         student_serializer = StudentSerializer(student)
#         return Response(student_serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         # Handle invalid data (e.g., return an error response)
#         print(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_student(request):
    try:
        # Deserialize request data into StudentCreateSerializer
        serializer = StudentCreateSerializer(data=request.data)

        # Validate the serializer data
        if serializer.is_valid():
            # Save the validated data to create a new Student instance
            serializer.save()

            # Return success response with serialized data of the created student
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return error response with validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        # Return error response if an exception occurs during creation process
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_student(request, pk):
    try:
        # Retrieve the Student instance by primary key (pk)
        student = Student.objects.get(pk=pk)

        # Serialize the Student instance
        serializer = StudentSerializer(student)

        # Return success response with serialized data of the retrieved student
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Student.DoesNotExist:
        # Return error response if the Student instance does not exist
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Return error response if an exception occurs during retrieval process
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_students_all(request):
    try:
        # Get all delivery_partners
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)

        return Response({
            'data': serializer.data,
        })

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response({'message': 'Student was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_student(request, pk):
    try:
        # Retrieve the Student instance by primary key (pk)
        student = Student.objects.get(pk=pk)

        # Deserialize request data into StudentSerializer with the instance to update
        serializer = StudentSerializer(student, data=request.data)

        # Validate the serializer data
        if serializer.is_valid():
            # Save the validated data to update the Student instance
            serializer.save()

            # Return success response with serialized data of the updated student
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Return error response with validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Student.DoesNotExist:
        # Return error response if the Student instance does not exist
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Return error response if an exception occurs during update process
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)