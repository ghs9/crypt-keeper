#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Length of vector array that will be used for encryption/decryption.
 */
#define VECTOR_LENGTH 256

/**
 * Key-scheduling algorithm (KSA).
 *
 * @param key string
 * @param S an array of ints representing permutation array (this is out parameter)
 */
void ksa (char[], int[]);


/**
 * Pseudo-random generation algorithm (PRGA).
 *
 * @param key string
 * @param PRGA an array of ints representing modification of array S
 * after modifying elements by using  key
 * @param data_len short int representing length of data that needs to be
 * processed
 */
void prga (char[], int[], short int);


/**
 * Encrypting data
 *
 * @param key string
 * @param data char array with data that needs to be encoded
 * @param result char array in which encoded data will be stored
 * @param PRGA int array keystream
 */
void rc4_encrypt (char *, char *, char *, int *);

/**
 * Decrypting data
 *
 * @param key string
 * @param data char array with data that needs to be decoded
 * @param result char array in which decoded data will be stored
 * @param PRGA int array keystream
 */
void rc4_decrypt (char *, char *, char *, int *);

void ksa (char key[], int S[]) {
  int keylength = strlen (key);
  int i = 0;
  int j = 0;
  int temp = 0;
  for (i = 0; i < VECTOR_LENGTH; i++)
    S[i] = i;

  for (i = 0; i < VECTOR_LENGTH; i++)
    {
      j = (j + S[i] + key[i % keylength]) % VECTOR_LENGTH;
      temp = S[j];
      S[j] = S[i];
      S[i] = temp;
    }
}

void prga (char key[], int PRGA[], short int data_len) {
  int S[VECTOR_LENGTH];
  int i = 0;
  int j = 0;
  int counter = 0;
  int temp = 0;
  ksa (key, S);
  for (counter = 0; counter < data_len; counter++) {
      i = (i + 1) % VECTOR_LENGTH;
      j = (j + S[i]) % VECTOR_LENGTH;
      temp = S[i];
      S[i] = S[j];
      S[j] = temp;

      PRGA[counter] = S[(S[i] + S[j]) % VECTOR_LENGTH];
  }
}

void rc4_encrypt (char *key, char *data, char *result, int *PRGA) {
  int i;
  int encoded = 0;
  int data_len = strlen(data);
  char temp_current[3];
  char *pointer = result;

  temp_current[2] = '\0';

  for (i = 0; i < data_len; i++) {
      encoded = PRGA[i] ^ data[i];
      sprintf (temp_current, "%02x", encoded);
      memcpy (pointer, temp_current, 2);
      pointer += 2;
  }
  pointer = NULL;
}


void rc4_decrypt (char *key, char *data, char *result, int *PRGA) {
  int i = 0;
  int data_len = strlen (data);
  int encoded = 0;
  int decoded;
  char *pointer = data;
  char *out_pointer = result;
  char current[3];

  current[2] = '\0';

  while (*pointer != '\0') {
      unsigned int test;

      memcpy (current, pointer, 2);
      pointer += 2;
      sscanf (current, "%x", &test);
      decoded = PRGA[i] ^ test;
      sprintf (out_pointer, "%c", decoded);
      i++;
      out_pointer++;
  }

  *out_pointer = '\0';
}

int main (int argc, char **args) {
  char *key;
  char *dataName;
  char *result = NULL;
  char *decrypted;
  FILE *inputF;
  int PRGA[VECTOR_LENGTH];
  int data_len;
  char buffer[256];
  key = malloc (strlen (args[1]));
  memcpy (key, args[1], strlen (args[1]));

  dataName = malloc (strlen (args[2]));
  memcpy (dataName, args[2], strlen (args[2]));
  inputF = fopen(dataName, "rb");
  fseek(inputF, 0, SEEK_END);
  long fsize = ftell(inputF);
  fseek(inputF, 0, SEEK_SET);
  char *data = malloc(fsize + 1);
  fread(data, fsize, 1, inputF);
  printf("%s",data);
  data_len = strlen(data);
  prga(key, PRGA, data_len);
  fseek(inputF,0, SEEK_SET);
  free (data);
  while(fgets(buffer, sizeof buffer, inputF) != NULL) {
    printf("LINE : %s", buffer);
    result = malloc (strlen (buffer) * 2);
    decrypted = malloc (strlen (buffer));

    rc4_encrypt (key, buffer, result, PRGA);
    printf ("ENCRYPTED DATA : %s\n", result);

    //rc4_decrypt (key, result, decrypted, PRGA);
    //printf ("DECRYPTED DATA : %s\n", decrypted);

    free(result);
    free(decrypted);
  }

  free (dataName);
  free (key);

  exit (EXIT_SUCCESS);
}
