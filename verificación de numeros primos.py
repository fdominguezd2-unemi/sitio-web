{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Welcome To Colaboratory",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/fdominguezd2-unemi/sitio-web/blob/main/verificaci%C3%B3n%20de%20numeros%20primos.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0edc95b5"
      },
      "source": [
        "```markdown\n",
        "# Verificador de Números Primos\n",
        "\n",
        "Este programa permite verificar si un número ingresado por el usuario es primo. El menú interactivo se ejecutará repetidamente hasta que el usuario decida salir.\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "748b6680"
      },
      "source": [
        "def es_primo(num):\n",
        "    \"\"\"\n",
        "    Verifica si un número es primo.\n",
        "    Un número primo es un número natural mayor que 1 que no tiene divisores positivos\n",
        "    más que 1 y él mismo.\n",
        "\n",
        "    Args:\n",
        "        num (int): El número entero a verificar.\n",
        "\n",
        "    Returns:\n",
        "        bool: True si el número es primo, False en caso contrario.\n",
        "    \"\"\"\n",
        "    # Los números menores o iguales a 1 no son primos por definición.\n",
        "    if num <= 1:\n",
        "        return False\n",
        "    # Itera desde 2 hasta la raíz cuadrada del número. Si el número tiene un divisor,\n",
        "    # siempre habrá uno menor o igual a su raíz cuadrada.\n",
        "    for i in range(2, int(num**0.5) + 1):\n",
        "        # Si el número es divisible por 'i', no es primo.\n",
        "        if num % i == 0:\n",
        "            return False\n",
        "    # Si no se encontraron divisores en el rango, el número es primo.\n",
        "    return True\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b975b004",
        "outputId": "ca93d36b-f033-43e5-c562-f83407c576bf"
      },
      "source": [
        "def menu_primos():\n",
        "    \"\"\"\n",
        "    Implementa un menú interactivo para verificar números primos.\n",
        "    Permite al usuario ingresar números y verificar su primalidad repetidamente\n",
        "    hasta que elija salir.\n",
        "    \"\"\"\n",
        "    # Lista para almacenar los resultados de cada consulta.\n",
        "    resultados_consultas = []\n",
        "\n",
        "    # El bucle principal del menú se ejecuta continuamente hasta que el usuario decida salir.\n",
        "    while True:\n",
        "        print(\"\\n--- Menú Verificador de Números Primos ---\")\n",
        "        print(\"1. Verificar si un número es primo\")\n",
        "        print(\"2. Salir\")\n",
        "\n",
        "        # Solicita la opción al usuario.\n",
        "        opcion = input(\"Ingrese su opción: \")\n",
        "\n",
        "        # Procesa la opción seleccionada.\n",
        "        if opcion == '1':\n",
        "            try:\n",
        "                # Solicita al usuario un número y lo convierte a entero.\n",
        "                numero_usuario = int(input(\"Ingrese un número entero: \"))\n",
        "                # Llama a la función es_primo para verificar.\n",
        "                es_primo_resultado = es_primo(numero_usuario)\n",
        "\n",
        "                if es_primo_resultado:\n",
        "                    mensaje = f\"El número {numero_usuario} ES un número primo.\"\n",
        "                else:\n",
        "                    mensaje = f\"El número {numero_usuario} NO es un número primo.\"\n",
        "\n",
        "                print(mensaje)\n",
        "                # Guarda el número y el resultado en la lista.\n",
        "                resultados_consultas.append(f\"Número: {numero_usuario}, Primo: {es_primo_resultado}\")\n",
        "\n",
        "            except ValueError:\n",
        "                # Maneja el error si el usuario no ingresa un número entero válido.\n",
        "                print(\"Entrada inválida. Por favor, ingrese un número entero válido.\")\n",
        "        elif opcion == '2':\n",
        "            # Si la opción es '2', sale del bucle y termina el programa.\n",
        "            print(\"¡Gracias por usar el verificador de números primos! Adiós.\")\n",
        "\n",
        "            # Muestra todos los resultados guardados antes de salir.\n",
        "            if resultados_consultas:\n",
        "                print(\"\\n--- Historial de Consultas ---\")\n",
        "                for resultado in resultados_consultas:\n",
        "                    print(resultado)\n",
        "            else:\n",
        "                print(\"No se realizaron consultas en esta sesión.\")\n",
        "            break\n",
        "        else:\n",
        "            # Si la opción no es '1' ni '2', informa al usuario de una opción inválida.\n",
        "            print(\"Opción inválida. Por favor, intente de nuevo.\")\n",
        "\n",
        "# Ejecutar el menú interactivo cuando se corre el script.\n",
        "menu_primos()\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "--- Menú Verificador de Números Primos ---\n",
            "1. Verificar si un número es primo\n",
            "2. Salir\n"
          ]
        }
      ]
    }
  ]
}